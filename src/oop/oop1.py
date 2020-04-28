# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:##this is the base class
  pass

class FlightVehicle(Vehicle):##'Child' of Vehicle
  pass

class Starship(FlightVehicle):##'Child' of FlightVehicle and 'Grandchild' of Vehicle
  pass

class Airplane(FlightVehicle):##'Child' of FlightVehicle and 'Grandchild' of Vehicle
  pass

class GroundVehicle(Vehicle):##'Child' of Vehicle
  pass

class Car(GroundVehicle):##'Child' of GroundVehicle and 'Grandchild' of Vehicle
  pass

class Motorcycle(GroundVehicle):##'Child' of GroundVehicle and 'Grandchild' of Vehicle
  pass