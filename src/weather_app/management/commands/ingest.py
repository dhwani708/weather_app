from django.core.management.base import BaseCommand
import glob
import csv
import logging
import datetime
from django.db.models import Avg, Sum
from weather_app.models import Weather_detail, Statistics_detail
from django.db.models.functions import Substr

path_log_file = "weather_logs/logfile.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(path_log_file), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Helps for Data Ingestion"

    @staticmethod
    def read_weather_file(file_path):
        logger.info("Ingesting " + file_path)
        with open(file_path, "r", encoding="utf8") as file:
            return [row for row in csv.reader(file, delimiter="\t")]

    def get_weather_data(self, path="wx_data"):
        s_time = datetime.datetime.now()
        logger.info("Initiating Weather Data Ingestion process.")
        try:
            file_list = glob.glob(path + "/*.txt")
            weather = [
                Weather_detail(
                    date=str(row[0]),
                    max_temp=int(row[1]),
                    min_temp=int(row[2]),
                    precipitation=int(row[3]),
                    station_name=file_name[-15:-4],
                )
                for file_name, rows in (
                    (file, self.read_weather_file(file)) for file in file_list
                )
                for row in rows
            ]
            Weather_detail.objects.bulk_create(weather, 5000, ignore_conflicts=True)
            e_time = datetime.datetime.now()
            logger.info("Weather Data Ingestion process completed successfully")
            logger.info(
                f"Time taken: {(e_time - s_time).total_seconds()}\t Number of records inserted: {len(weather)}"
            )
        except Exception as err:
            logger.error(f"{err}")

    def get_statistics_data(self):
        try:
            result = (
                Weather_detail.objects.filter(
                    max_temp__gt=-9999, min_temp__gt=-9999, precipitation__gt=-9999
                )
                .values(
                    "station_name",
                    year=Substr("date", 1, 4),
                )
                .annotate(
                    max_temp_avg=Avg("max_temp"),
                    min_temp_avg=Avg("min_temp"),
                    ppt_sum=Sum("precipitation"),
                )
            )
            statistics = [
                Statistics_detail(
                    station_name=res["station_name"],
                    date=res["year"],
                    avg_max_temp=res["max_temp_avg"],
                    avg_min_temp=res["min_temp_avg"],
                    total_acc_ppt=res["ppt_sum"],
                )
                for res in result
            ]
            Statistics_detail.objects.bulk_create(
                statistics, 5000, ignore_conflicts=True
            )
            logger.info("Executed Successfully")
        except Exception as err:
            logger.error(f"{err}")

    def handle(self, *args, **kwargs):
        self.get_weather_data()
        self.get_statistics_data()
