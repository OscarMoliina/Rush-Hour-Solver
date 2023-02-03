(define (domain rush_hour)

(:requirements :strips :fluents :typing :adl :equality)

(:types
coche casilla - object
hor ver - coche
)

(:predicates
    (En ?co - coche ?ca - casilla)
    (Libre ?ca - casilla)
    (CabezaEn ?co - coche ?ca - casilla)
    (ColaEn ?co - coche ?ca - casilla)
    (DerechaDe ?c1 - casilla ?c2 - casilla)
    (ArribaDe ?c1 - casilla ?c2 - casilla)
    (ExtremoNS ?c - casilla)
    (ExtremoEO ?c - casilla)
)

(:action Mover_Derecha
    :parameters (?c - hor ?c1 - casilla ?c2 - casilla ?c3 - casilla ?c4 - casilla)
    :precondition (and
        (not (ExtremoEO ?c3))
        (Libre ?c4)
        (DerechaDe ?c4 ?c3)(En ?c ?c3)
        (CabezaEn ?c ?c3)(ColaEn ?c ?c1)
        (DerechaDe ?c2 ?c1)
        (En ?c ?c1)(En ?c ?c2)
    )
    :effect (and 
        (not (En ?c ?c1))(En ?c ?c4)(Libre ?c1)(not (Libre ?c4))
        (not (CabezaEn ?c ?c3))(CabezaEn ?c ?c4)(not (ColaEn ?c ?c1))(ColaEn ?c ?c2)
    )
)

(:action Mover_Izquierda
    :parameters (?c - hor ?c1 - casilla ?c2 - casilla ?c3 - casilla ?c4 - casilla)
    :precondition (and 
        (not (ExtremoEO ?c2))
        (DerechaDe ?c2 ?c1)
        (Libre ?c1)(En ?c ?c2)
        (CabezaEn ?c ?c4)(ColaEn ?c ?c2)
        (DerechaDe ?c4 ?c3)
        (En ?c ?c3)(En ?c ?c4)
    )
    :effect (and 
        (not (En ?c ?c4))(En ?c ?c1)(Libre ?c4)(not (Libre ?c1))
        (not (CabezaEn ?c ?c4))(CabezaEn ?c ?c3)(not (ColaEn ?c ?c2))(ColaEn ?c ?c1)
    )
)
(:action Mover_Arriba
    :parameters (?c - ver ?c1 - casilla ?c2 - casilla ?c3 - casilla ?c4 - casilla)
    :precondition (and
        (not (ExtremoNS ?c3))
        (ArribaDe ?c4 ?c3)
        (Libre ?c4)(En ?c ?c3)
        (CabezaEn ?c ?c3)(ColaEn ?c ?c1)
        (ArribaDe ?c2 ?c1)
        (En ?c ?c1)(En ?c ?c2)
    )
    :effect (and 
        (not (En ?c ?c1))(En ?c ?c4)(Libre ?c1)(not (Libre ?c4))
        (not (CabezaEn ?c ?c3))(CabezaEn ?c ?c4)(not (ColaEn ?c ?c1))(ColaEn ?c ?c2)
    )
)
(:action Mover_Abajo
    :parameters (?c - ver ?c1 - casilla ?c2 - casilla ?c3 - casilla ?c4 - casilla)
    :precondition (and
        (not (ExtremoNS ?c2))
        (ArribaDe ?c2 ?c1)
        (Libre ?c1)(En ?c ?c2)
        (CabezaEn ?c ?c4)(ColaEn ?c ?c2)
        (ArribaDe ?c4 ?c3)
        (En ?c ?c3)(En ?c ?c4)
    )
    :effect (and 
        (not (En ?c ?c4))(En ?c ?c1)(Libre ?c4)(not (Libre ?c1))
        (not (CabezaEn ?c ?c4))(CabezaEn ?c ?c3)(not (ColaEn ?c ?c2))(ColaEn ?c ?c1)
    )
)

)