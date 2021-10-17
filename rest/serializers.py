from rest_framework.serializers import ModelSerializer

from rest.models import Quote


class QuoteSerializers(ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


