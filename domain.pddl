(define (domain rush_hour)

(:requirements :strips :fluents :typing :adl :equality)

(:types
coche casilla posicion - object
posx posy - posicion
r h v - coche
)

(:predicates
    (En ?c - casilla ?x - posx ?y - posy)
    (Libre ?c - casilla)
    (Cabeza ?c - coche ?x - posx ?y - posy)
    (Cola ?c - coche ?x - posx ?y - posy)
)

(:functions

)

(:action Mover_Derecha
    :parameters ()
    :precondition (and )
    :effect (and )
)
(:action Mover_Izquierda
    :parameters ()
    :precondition (and )
    :effect (and )
)
(:action Mover_Arriba
    :parameters ()
    :precondition (and )
    :effect (and )
)
(:action Mover_Abajo
    :parameters ()
    :precondition (and )
    :effect (and )
)

)