from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.db.models import Count, Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from orders.models import Order, OrderLineItem
from products.models import Product
from reviews.models import Review
from .serializers import ProductSerializer, MonthlyEarning
from django.db.models.functions import TruncMonth, TruncYear
from itertools import groupby
from operator import itemgetter
from django.contrib.auth.decorators import login_required


def view_chart(View):
    def get(self, request, *args, **kwargs):
        return render(request, "chart.html")


def view_chart_orders(View):
    def get(self, request, *args, **kwargs):
        return render(request, "chart_orders.html")


class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # Load data from Database

        # data serializer to convert sql database in json
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        product_data = serializer.data

        # Need to made a list of product with own quantity taken datas from order line items
        product_name = Product.objects.all().values(
            "name").annotate(dcount=(Sum("orderlineitem__quantity")))

        list_product_name = list()
        quantity_product_sold = list()

        for name in product_name:
            list_product_name.append(name['name'])
            quantity_product_sold.append(name['dcount'])

        # calculate total earning by month
        earnings_by_month = OrderLineItem.objects.annotate(month=TruncMonth(
            'date')).values('month').annotate(Sum('total'))

        months_in_earning = list()
        earning = list()

        for entry in earnings_by_month:
            months_in_earning.append(entry['month'])
            earning.append(entry['total__sum'])

        count_orders = Order.objects.all().count()
        count_users = User.objects.all().count()

        # calculate number of orders by months

        number_of_orders_by_month = Order.objects.annotate(month=TruncMonth(
            'date')).values('month').annotate(total=Count('orderlineitem'))

        months_in_orders = list()
        orders_by_months = list()

        for entry in number_of_orders_by_month:
            months_in_orders.append(entry['month'])
            orders_by_months.append(entry['total'])

        # Counting score to made a chart with scores
        # aggregation Q & not working
        review_one_score = Review.objects.filter(rating=1).count()
        review_two_score = Review.objects.filter(rating=2).count()
        review_three_score = Review.objects.filter(rating=3).count()
        review_four_score = Review.objects.filter(rating=4).count()
        review_five_score = Review.objects.filter(rating=5).count()

        # Sum total charts
        negative_rating = review_one_score + review_two_score
        medium_rating = review_three_score
        positive_rating = review_four_score + review_five_score

        # calculate number of product sold by product an made a pie chart

        #
        label_rating = ["Negative", "Medium", "Positive"]

        # Assign data
        data = {
            "label_rating": label_rating,
            "number_of_orders_by_month": number_of_orders_by_month,
            "months_in_earning": months_in_earning,
            "earning": earning,
            "months_in_orders": months_in_orders,
            "orders_by_months": orders_by_months,
            "product_name": list_product_name,
            "quantity_product_sold": quantity_product_sold,
            "score_rating": [negative_rating, medium_rating, positive_rating],
        }

        return Response(data)
