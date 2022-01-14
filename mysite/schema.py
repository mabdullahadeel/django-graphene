import graphene
from cars.models import Manufacturer, Car, ManufacturerBaseCountry
from graphene_django import DjangoObjectType


class ManufacturerBaseCountryType(DjangoObjectType):
    class Meta:
        model = ManufacturerBaseCountry
        fields = ('id', 'name')

class ManufacturerType(DjangoObjectType):
  class Meta:
    model = Manufacturer
    fields = ('id', 'name', 'logo_url', 'base_country')


class CarType(DjangoObjectType):
  class Meta:
    model = Car
    fields = ('id', 'name', 'features_description', 'manufacturer', 'color')




class Query(graphene.ObjectType):
    all_cars = graphene.List(CarType)
    base_country = graphene.List(ManufacturerBaseCountryType)
    manufacturer_by_name = graphene.Field(ManufacturerType, name=graphene.String(required=True))

    
    def resolve_all_cars(root, info):
        return Car.objects.select_related('manufacturer').all()

    
    def resolve_base_country(root, info):
        return ManufacturerBaseCountry.objects.all()

    def resolve_manufacturer_by_name(root, info, name):
        try:
            return Manufacturer.objects.get(name=name)
        except Manufacturer.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)