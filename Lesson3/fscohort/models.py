from django.db import models


class Students(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=30)
    Number = models.IntegerField()
    
    def __str__(self) -> str:
        return (f"{self.Number}-{self.FirstName}")
    class Meta:
        ordering = ["Number"]
        verbose_name_plural = "Student_List"
        db_table = "Student_Table"
        