from django.test import TestCase

from example.models import example
# Create your tests here.
class exampletest(TestCase):
      def createexample(self,fname="janakiraman",fphone="Non numerical"):
          return example.objects.create(name=fname,phone=fphone)
      def test_example(self):
          r=self.createexample()
          self.assertTrue(isinstance(r,example))
          
	  
          
         
