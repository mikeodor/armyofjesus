from import_export import resources
from .models import prayer,pastors,Ministries,breadcrumb,LatestSermon,slide

class PersonResource(resources.ModelResource):
    class Meta:
        model = prayer
class PersonResource(resources.ModelResource):
    class Meta:
        model = Ministries
        
class PersonResource(resources.ModelResource):
    class Meta:
        model = pastors
        
        
class PersonResource(resources.ModelResource):
    class Meta:
        model = breadcrumb
        
class PersonResource(resources.ModelResource):
    class Meta:
        model = LatestSermon
        
class PersonResource(resources.ModelResource):
    class Meta:
        model = slide
