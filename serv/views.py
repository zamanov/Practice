from .models import Cell, Object
from rest_framework import status, generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CellSerializer, ObjectSerializer

class CellList(generics.ListCreateAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('sector', 'row', 'is_blocked','cell_name')
    
class ObjectList(generics.ListCreateAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('object_name', 'cell', 'owner')
    
    def post(self, request):
		serializer = ObjectSerializer(data=request.DATA)
		if serializer.is_valid():
			ocell = Cell.objects.get(pk=request.data['cell'])
			if cell.is_blocked:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			else:
				cell.is_blocked=True
				cell.save()	 
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

@api_view(['GET','PUT','DELETE'])
def cell_detail(request,pk):
	try:
		cell = Cell.objects.get(pk=pk)
	except Cell.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = CellSerializer(cell)
		return Response(serializer.data)
	elif request.method == 'PUT':
		serializer = CellSerializer(cell, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		cell.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def object_detail(request,pk):
	try:
		object = Object.objects.get(pk=pk)
	except Object.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = ObjectSerializer(object)
		return Response(serializer.data)
	elif request.method == 'PUT':
		serializer = ObjectSerializer(object, data=request.DATA)
		if serializer.is_valid():
			new_cell = Cell.objects.get(pk=request.data['cell'])
			if new_cell.id==object.cell.id:
				serializer.save()
				return Response(serializer.data)
			elif not(new_cell.is_blocked):
				cell = Cell.objects.get(pk=object.cell.id)
				cell.is_blocked = False
				cell.save()
				new_cell.is_blocked = True
				new_cell.save()
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		cell = Cell.objects.get(pk=object.cell.id)
		cell.is_blocked=False
		cell.save()
		object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
