(define (problem rush_hour) (:domain rush_hour)
(:objects
 R - hor
 C13 C23 C33 - casilla
 C12 C22 C32 - casilla
 C11 C21 C31 - casilla
)

(:init
    (ArribaDe C13 C12)(ArribaDe C12 C11)(ArribaDe C23 C22)(ArribaDe C22 C21)(ArribaDe C33 C32)(ArribaDe C32 C31)
    (DerechaDe C31 C21)(DerechaDe C21 C11)(DerechaDe C32 C22)(DerechaDe C22 C12)(DerechaDe C33 C23)(DerechaDe C23 C13)
    (En R C12)(En R C22)
    (Libre C11)(Libre C13)(Libre C21)(Libre C31)(Libre C32)(Libre C33)(Libre C23)
    (CabezaEn R C22)(ColaEn R C12)
    (Extremo C13)(Extremo C12)(Extremo C11)(Extremo C23)(Extremo C33)(Extremo C32)(Extremo C31)(Extremo C21)
)

(:goal (and
    (CabezaEn R C32)
))
)
