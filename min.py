class Student:
      def __init__ (self,regno,name,age):
             self.regno=regno
             self.name=name
             self.age=age
      def study(self):
        return "i am studying"
      def play(self):
        return"i am playing"
      def Discuss(self):
        return"i am discussing"
      def __str__(self):
        return f"my name is {self.name}"
student_1=Student("S21B13/044","sarah",32)
print(student_1)
print(student_1.study())
print(student_1.play())
print(student_1.Discuss())
