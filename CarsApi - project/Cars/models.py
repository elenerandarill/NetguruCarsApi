from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    rates_counter = models.IntegerField(default=0)    # counts the amount of votes, eg. 10
    total_rates = models.IntegerField(default=0)      # summs up the rate, like 41 ponts total
    average_rate = models.FloatField(default=0)     # total_rates / rates_counter, eg. 4.1

    def __str__(self):
        return f"Car - model name: {self.model_name}, make: {self.make}, average rate: {self.average_rate} "

    def rate(self, instance, validated_data):
        instance.rates_counter += 1
        instance.total_rates += validated_data['rate']
        instance.average_rate = round(self.total_rates / self.rates_counter, 1)
        instance.save()
        return instance
