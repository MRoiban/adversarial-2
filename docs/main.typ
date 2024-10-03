#import "@preview/equate:0.2.0": equate
#import "@preview/showybox:2.0.1": showybox
#import "@preview/lovelace:0.3.0": *
#import "@preview/ilm:1.1.2": *



#show: ilm.with(
  title: [Rapport Projet F311: Adversarial Search],
  author: "Roiban Marius-Alexandru",
  date: datetime(year: 2024, month: 10, day: 03),
  abstract: [],
  preface: [],
  figure-index: (enabled: true),
  table-index: (enabled: true),
  listing-index: (enabled: true)
)

#let showbox(title, body) = box()[
  #showybox(
    shadow: (
      offset:3.5pt
    ), title: title,
    [#body]
  )
]


#let pseudocodeblock(title, code) = box[#text(
  font: "FiraCode Nerd Font Mono", 
  ligatures: true
)[
  #showybox(
    shadow: (
      offset: 3.5pt
  ),
  title: title,
  [#code]
  )
]]

#let CQFD = box[$space square.filled$]


= Implementation
== Minimax
For the minimax algorithm to finish, an end condition must be set:
  1. Have we reached the maximum depth?
  2. Are we on the exit?
  3. Have all the gems been collected?

If all of the conditions have been met, then the algorithm can return the Heuristic. 



#showbox([*The Heuristic Function*], [
To let the minimax algorithm know it is going in the right direction 

*Exit Heuristic *\
[(closest_exit.x + closest_exit.y) - distance_to_exit + is_exit_tile]
 

*Gem Heuristic*\
[(closest_gem.x + closest_gem.y) - distance_to_gem + is_gem_tile]

- is_gem_tile = 10 points
- is_exit_tile = 2 points
])

