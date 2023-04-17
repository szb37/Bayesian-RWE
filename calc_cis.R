### Calc credible intevral 
# https://easystats.github.io/bayestestR/articles/credible_interval.html
library(bayestestR)

posterior <- distribution_beta(10000, 18, 6)
ci_hdi <- ci(posterior, method = "HDI")