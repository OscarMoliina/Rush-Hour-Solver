(define (problem rush_hour) (:domain rush_hour)
(:objects
	R H1 - hor
	V1 - ver
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
	
	(DerechaDe C12 C11) (DerechaDe C22 C21) (DerechaDe C32 C31) (DerechaDe C42 C41) (DerechaDe C52 C51) (DerechaDe C62 C61) 
	(DerechaDe C13 C12) (DerechaDe C23 C22) (DerechaDe C33 C32) (DerechaDe C43 C42) (DerechaDe C53 C52) (DerechaDe C63 C62) 
	(DerechaDe C14 C13) (DerechaDe C24 C23) (DerechaDe C34 C33) (DerechaDe C44 C43) (DerechaDe C54 C53) (DerechaDe C64 C63) 
	(DerechaDe C15 C14) (DerechaDe C25 C24) (DerechaDe C35 C34) (DerechaDe C45 C44) (DerechaDe C55 C54) (DerechaDe C65 C64) 
	(DerechaDe C16 C15) (DerechaDe C26 C25) (DerechaDe C36 C35) (DerechaDe C46 C45) (DerechaDe C56 C55) (DerechaDe C66 C65) 

	(ExtremoNS C11) (ExtremoNS C12) (ExtremoNS C13) (ExtremoNS C14) (ExtremoNS C15) (ExtremoNS C16) (ExtremoNS C61) (ExtremoNS C62) (ExtremoNS C63) (ExtremoNS C64) (ExtremoNS C65) (ExtremoNS C66) 
	(ExtremoEO C11) (ExtremoEO C21) (ExtremoEO C31) (ExtremoEO C41) (ExtremoEO C51) (ExtremoEO C61) (ExtremoEO C16) (ExtremoEO C26) (ExtremoEO C36) (ExtremoEO C46) (ExtremoEO C56) (ExtremoEO C66) 
	(En R C41) (En R C42) (CabezaEn R C42) (ColaEn R C41)
	(En H1 C12) (En H1 C13) (CabezaEn H1 C13) (ColaEn H1 C12)
	(En V1 C21) (En V1 C31) (CabezaEn V1 C31) (ColaEn V1 C21)
	(Libre C11) (Libre C14) (Libre C15) (Libre C16) (Libre C22) (Libre C23) (Libre C24) (Libre C25) (Libre C26) (Libre C32) (Libre C33) (Libre C34) (Libre C35) (Libre C36) (Libre C43) (Libre C44) (Libre C45) (Libre C46) (Libre C51) (Libre C52) (Libre C53) (Libre C54) (Libre C55) (Libre C56) (Libre C61) (Libre C62) (Libre C63) (Libre C64) (Libre C65) (Libre C66) 
)

(:goal (and
	(CabezaEn R C46)
))
)