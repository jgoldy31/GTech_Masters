#import relevant libraries for data manipulation and visualization
library(dplyr)
library(tidyr)
library(ggplot2)

#Initialize a vector to store number of turns
turn_vec= c()
#Initilialize dataframe for tracking pot values
pot_track = data.frame(
  iteration = c(0),
  turn = c(0),
  pot_val = c(0)
)
#run 20k simulations
for(i in 1:20000){
iters = c()
pot_values = c()
t_vals = c()
#initialize values for players and pot
a = 4
b = 4
pot = 2

#set value to zero for turns, true false for running
running = TRUE
turns = 0
#while loop for each iteration
while (running) {
  #generate a dice roll
  dice =ceiling(6 * runif(1))
  #update turns
  turns = turns + 1
  
  if(dice == 1){
    #nothing, proceed
  }else if(dice == 2){
    #player gets all the coins in the pot, use mod to see which player we are on
    if(turns %% 2 == 0){
      a = a + pot
    }else{
      b = b + pot
    }
    #Set pot to zero
    pot =0
    
  }else if(dice == 3){
    #player gets half the coins in the pot rounded down, use mod to see which player we are on
    if(turns %% 2 == 0){
      a = a + floor(.5 * pot)
    }else{
      b = b +  floor(.5 * pot)
    }
    #Set pot to zero
    pot = pot -  floor(.5 * pot)
    
  }else{
    #put one in pot, see if player is out
    if(turns %% 2 == 0){
      a = a - 1
      
      if(a < 0){
        running = FALSE
      }
    }else{
      b = b - 1
      
      if(b < 0){
        running = FALSE
      }
    }
    pot = pot + 1
  }
  
  #store values
  iters = c(iters, i)
  pot_values = c(pot_values, pot)
  t_vals = c(t_vals, turns)
  
}
#store values
this_pot_track = data.frame(
  iteration = iters,
  pot_val = pot_values,
  turn = t_vals 
)
pot_track = rbind(pot_track, this_pot_track) 
#account for one dice roll being half a turn, ceiling so if A was last still counts as a turn
turn_vec = c(turn_vec, ceiling(turns * .5))
}

pot_track = pot_track %>% 
  mutate(iteration = as.factor(iteration))
#randomly select 5 iterations to view pot fluctuation
rand_iters = sample(1:20000, 5)
p_track =pot_track %>% 
filter(iteration %in% rand_iters)
ggplot(p_track, aes(x = turn, y = pot_val, color = iteration)) +
  geom_line(size = 2.2)+
  ylab('Pot Value')+
  xlab('Dice Roll of Game')+
  ylim(0,8)+
  theme(legend.position="none")
pot_graphic

#create histogram of distribution of turns
h <- hist(turn_vec,breaks = 50, plot = FALSE)
p <- plot(h, ylab = 'Occurences', xlab = 'Turns', col = '#8ee2e7', main = 'Turns Per Game Histogram')

#look at central tendency measures for turns
median(turn_vec)
IQR(turn_vec)
mode(turn_vec)
boxplot(turn_vec)
fivenum(turn_vec)

#Check runif to see if uniform
tosses = ceiling(6 * runif(20000))
table(tosses)

