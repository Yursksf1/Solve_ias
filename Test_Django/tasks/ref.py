class Item(models.Model):
    name = models.CharField(max_length=500)
    startDate = models.DateTimeField("Start Date", unique="true")
    endDate = models.DateTimeField("End Date")     

    def save(self, *args, **kwargs):
        try:
            Item.objects.get(Q(startDate__range=(self.startDate,self.endDate))
                            |Q(endDate__range=(self.startDate,self.endDate))
                            |Q(startDate__lt=self.startDate,endDate__gt=self.endDate))
            #raise some save errorexcept ValueError:
            raise Http404("Date out on range")
        except Item.DoesNotExist:
            super(Item,self).save(*args,**kwargs)


class Booked(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    resource = models.CharField(max_length=500)

    def clean(self):
        if Booked.objects.filter(
             Q(start_date__gte=self.start_date, start_date__lt=self.end_date)
           | Q(end_date__gt=self.start_date, end_date__lte=self.end_date)
        ).exists():
            raise ValidationError("Overlapping dates")

class Dimension_Item(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        # get number of items that have an overlapping start date
        dimension_items_overlapping_start = Dimension_Item.objects.filter(start_date__gte=self.start_date, start_date__lte=self.end_date).count()

        # get number of items that have an overlapping end date
        dimension_items_overlapping_end = Dimension_Item.objects.filter(end_date__gte=self.start_date, end_date__lte=self.end_date).count()

        overlapping_dimension_items_present = dimension_items_overlapping_start > 0 or dimension_items_overlapping_end > 0

        if overlapping_dimension_items_present:
            return 
        else:
            super(Dimension_Item, self).save(*args, **kwargs) # Call the "real" save() method.



