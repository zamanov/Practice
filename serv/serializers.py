from rest_framework import serializers
from models import Cell, Object

class CellSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cell
		fields = ('cell_name','is_blocked', 'sector', 'row')
class ObjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Object
		fields = ('object_name','cell', 'owner')    
