rm(list = ls())
n <- 500000
nducks <- 4


check_position <- function(duck1, duck2) { # duck1, duck2 -> TRUE (front), FALSE (back)
  if (duck1 <= pi) {
    if ((duck2 >= duck1) & (duck2 < duck1 + pi)) {
      return(TRUE) # At front
    }
    else {
      return(FALSE) # At back
    }
  }
  else {
    if ((duck2 >= (duck1 + pi) %% (2 * pi)) & (duck2 < duck1)) {
      return(FALSE) # At back
    }
    else {
      return(TRUE) # At front
    }
  }
}


check_duck <- function(ducks) { # ducks:vector -> Boolean
  for (i in seq_along(ducks)) {
    first <- ducks[i]
    other_ducks <- ducks[-i]
    side <- matrix(nrow = length(other_ducks))
    for (j in seq_along(other_ducks)) {
      side[j] <- check_position(first, other_ducks[j])
    }
    if (any(all(side), all(!side))) {
      return(TRUE)
    }
  }
  return(FALSE)
}


store <- matrix(nrow = n, ncol = nducks + 1)
for (i in 1:n) {
  store[i, 1:nducks] <- runif(nducks, min = 0, max = 2 * pi)
  store[i, nducks + 1] <- check_duck(store[i, 1:nducks])
}


mean(store[, nducks + 1])
