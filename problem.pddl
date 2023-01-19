(define (problem rush_hour) (:domain rush_hour)
(:objects
    R - hor
    C61 C62 C63 C64 C65 C66 - casilla
	C51 C52 C53 C54 C55 C56 - casilla
	C41 C42 C43 C44 C45 C46 - casilla
	C31 C32 C33 C34 C35 C36 - casilla
	C21 C22 C23 C24 C25 C26 - casilla
	C11 C12 C13 C14 C15 C16 - casilla
)

(:init
    (ArribaDe C21 C11) (ArribaDe C31 C21) (ArribaDe C41 C31) (ArribaDe C51 C41) (ArribaDe C61 C51) 
	(ArribaDe C22 C12) (ArribaDe C32 C22) (ArribaDe C42 C32) (ArribaDe C52 C42) (ArribaDe C62 C52) 
	(ArribaDe C23 C13) (ArribaDe C33 C23) (ArribaDe C43 C33) (ArribaDe C53 C43) (ArribaDe C63 C53) 
	(ArribaDe C24 C14) (ArribaDe C34 C24) (ArribaDe C44 C34) (ArribaDe C54 C44) (ArribaDe C64 C54) 
	(ArribaDe C25 C15) (ArribaDe C35 C25) (ArribaDe C45 C35) (ArribaDe C55 C45) (ArribaDe C65 C55) 
	(ArribaDe C26 C16) (ArribaDe C36 C26) (ArribaDe C46 C36) (ArribaDe C56 C46) (ArribaDe C66 C56) 
	(DerechaDe C12 C11) (DerechaDe C22 C21) (DerechaDe C32 C31) (DerechaDe C42 C41) (DerechaDe C52 C51) 
	(DerechaDe C13 C12) (DerechaDe C23 C22) (DerechaDe C33 C32) (DerechaDe C43 C42) (DerechaDe C53 C52) 
	(DerechaDe C14 C13) (DerechaDe C24 C23) (DerechaDe C34 C33) (DerechaDe C44 C43) (DerechaDe C54 C53) 
	(DerechaDe C15 C14) (DerechaDe C25 C24) (DerechaDe C35 C34) (DerechaDe C45 C44) (DerechaDe C55 C54) 
	(DerechaDe C16 C15) (DerechaDe C26 C25) (DerechaDe C36 C35) (DerechaDe C46 C45) (DerechaDe C56 C55) 
    (En R C21)(En R C22)
    (Libre C23)(Libre C24)(Libre C25)(Libre C26)
    (CabezaEn R C22)(ColaEn R C21)
    (Extremo C21)(Extremo C26)
)

(:goal (and
    (CabezaEn R C26)
))
)
