from rest_framework import serializers
from rest_framework.response import Response
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields =['id','username','email','password']
		#extra_kwargs={'password':{'write_only':True}}
	def create(self,validated_data):
		print("hii")
		extra_kwargs={'email':{'validators':[EmailValidator,]}},
		email=validated_data.get('email','')
		if User.objects.filter(email=email):
			print("bye")
			raise serializers.ValidationError({
				'email':('email exists')
			})
		user=User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
		return user
		
		