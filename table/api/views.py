from rest_framework import generics, pagination
from rest_framework.response import Response

from ..models import SimpleTable
from .serializers import SimpleTableListSerializers


# class PageNumberPaginationWithCount(pagination.PageNumberPagination):
#
#     def get_paginated_response(self, data):
#         return Response({
#             'count': self.page.paginator.count,
#             'next': self.get_next_link(),
#             'previous': self.get_previous_link(),
#             'total_pages': self.page.paginator.num_pages,
#             'results': data
#         })


class ListSimpleTableView(generics.ListAPIView):

    serializer_class = SimpleTableListSerializers
    queryset = SimpleTable.objects.all().order_by('name')
    # pagination_class = PageNumberPaginationWithCount
