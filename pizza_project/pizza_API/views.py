from rest_framework.views import APIView, Response
from .serializors import PizzaSerializor,sizeSerializer
from rest_framework import status
from .models import Pizza,Size_item
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination


class PizzaAPI(APIView):

    def post(self, request):
        mutable_data = request.data
        mutable_data['Toppings'] = list(map(lambda item: {"name": item}, mutable_data.get('Toppings', [])))
        serialized_pizza = PizzaSerializor(data=mutable_data)
        if serialized_pizza.is_valid():
            serialized_pizza.save()
            return Response({"message": "pizza added "}, status=status.HTTP_201_CREATED)
        return Response(data=serialized_pizza.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pizza = get_object_or_404(Pizza, id=request.data.get('id', None))
        pizza.delete()
        return Response({"message": "pizza removed "}, status=status.HTTP_200_OK)

    def put(self, request):
        pizza = get_object_or_404(Pizza, id=request.data.get('id', None))
        Toppings = request.data.get('Toppings', {})

        data_mutable = request.data
        data_mutable['Toppings'] = Toppings.get("data", [])
        data_mutable['Toppings'] = list(map(lambda item: {"name": item}, data_mutable['Toppings']))

        serialized_pizza = PizzaSerializor(instance=pizza, data=data_mutable, partial=True,
                                           context={'add_Topping': Toppings.get('add_Topping', True)})
        if serialized_pizza.is_valid():
            serialized_pizza.save()
            return Response({"message": "pizza modified "}, status=status.HTTP_200_OK)
        return Response(data=serialized_pizza.errors, status=status.HTTP_400_BAD_REQUEST)


class Pizza_ListAPI(ListAPIView):
    serializer_class = PizzaSerializor
    pagination_class = PageNumberPagination

    def get_queryset(self):
        size_asked = self.request.query_params.get("size", None)
        type_asked = self.request.query_params.get("type", None)

        if size_asked and type_asked:
            return Pizza.objects.filter(size__iexact=size_asked).filter(Type__iexact=type_asked)
        elif size_asked:
            return Pizza.objects.filter(size__iexact=size_asked)
        elif type_asked:

            return Pizza.objects.filter(Type__iexact=type_asked)
        else:
            return Pizza.objects.all()




class sizeAPI(APIView):

    def post(self,request):
        size_serialized = sizeSerializer(request.data)
        if size_serialized.is_valid():
            size_serialized.save()
            return Response({"message":"size added"},status=status.HTTP_201_CREATED)
        return Response(size_serialized.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        size = get_object_or_404(Size_item,name=request.data.get("name",""))
        size.delete()
        return Response({"message":"size removed"},status=status.HTTP_200_OK)


