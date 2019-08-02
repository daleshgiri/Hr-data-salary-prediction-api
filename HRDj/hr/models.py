from django.db import models

class HR(models.Model):                                         
    satisfaction_level = models.FloatField()
    last_evaluation = models.FloatField()
    number_project = models.FloatField()
    average_montly_hours = models.FloatField(default=0)
    time_spend_company = models.FloatField()
    Work_accident = models.FloatField()
    left = models.FloatField()
    promotion_last_5years = models.FloatField()
    Department = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    def to_dict(self):
        return {
            'satisfaction_level':self.satisfaction_level ,
            'last_evaluation':self.last_evaluation ,
            'number_project':self.number_project ,
            'average_montly_hours':self.average_montly_hours ,
            'time_spend_company':self.time_spend_company ,
            'Work_accident':self.Work_accident ,
            'left':self.left ,
            'promotion_last_5years':self.promotion_last_5years ,
            'Department':self.Department ,
            'salary':self.salary 
        }                                          

