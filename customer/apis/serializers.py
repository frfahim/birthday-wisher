from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from customer.models import Customer


class CustomerCreateSerializer(serializers.Serializer):
	name = serializers.CharField()
	birthdate = serializers.DateField()
	email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=Customer.objects.all())])

	def validate_email(self, value):
		if Customer.objects.filter(email__iexact=value).exists():
			raise serializers.ValidationError("Email Already exist")
		return value


class CustomerUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = [
			'name',
			'birthdate',
		]


class CustomerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Customer
		fields = [
			'id',
			'name',
			'birthdate',
			'email',
		]

		read_only_fields = ('id',)
