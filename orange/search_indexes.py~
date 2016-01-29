import datetime
from haystack import indexes
from orange.models import media_info

class media_infoIndex(indexes.SearchIndex, indexes.Indexable):
     
      text = indexes.CharField(document=True, use_template=True)
      media_info_date_release = indexes.DateField(model_attr='media_info_date_release')
      media_info_name = indexes.CharField(model_attr='media_info_name')

      def get_model(self):
          return media_info

      def index_queryset(self, using=None):
          return self.get_model().objects.filter(media_info_date_release__lte=datetime.datetime.now())
