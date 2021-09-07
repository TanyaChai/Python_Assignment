import time
import csv

from base import HackerNews


class HackerNewsCSV(HackerNews):
    """
    This class extends HackerNews
    """
    def run(self):
        """
        This function writes data to hackernews.csv
        :return: true
        """
        with open('hackernews.csv', mode='w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # Header portion of csv
            writer.writerow(['ID', 'Type', 'By', 'URL', 'Title'])
            # Writing each row in csv from self.data
            for item in self.data:
                writer.writerow(item)
        return True


start = time.time()
news_csv = HackerNewsCSV().run()
end = time.time()
total_time = end - start
print('It took {} seconds to complete'.format(total_time))
print('Find the csv file in the folder root!')

