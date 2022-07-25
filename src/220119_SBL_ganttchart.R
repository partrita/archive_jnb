library("ganttrify")
library(tidyverse)
library(Cairo)
df <- read.csv(file="C:/Users/KimTaeyoon/Documents/Jupyter/INPUT/220119_SBL_gantt.csv", header=T)
df

ganttrify(project = df,
          project_start_date = "2020-01",
          hide_wp = TRUE,
          by_date = TRUE,
          exact_date = TRUE,
          font_family = "Roboto Condensed")
