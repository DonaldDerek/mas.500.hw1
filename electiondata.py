import urllib2
import json
from bs4 import BeautifulSoup

class ElectionResults:

    def __init__(self, url):
        self.url = url

    def load(self):
        c = 0
        votes = []
        header = ''
        str_header = ''

        response = urllib2.urlopen(self.url)
        print "Fetching votes from archives.gov...[done]"

        html = response.read()
        soup = BeautifulSoup(html)
        table = soup.find_all('table')[1]

        for data in table:
            if c == 1:
                header = data
            elif c >= 5:
                if hasattr(data, 'get_text'):
                    v = data.get_text().split('\n')
                    v.pop()
                    votes.append(v[1:])
            c += 1

        f = open('election.cvs','w+')

        header = header.get_text().split('\n')[1:]
        header.pop()

        self.votes = []

        str_header = ','.join(header).encode('utf-8').strip()

        self.votes.append(str_header)

        f.write(str_header+"\n")

        for vote in votes:
            str_votes = ','.join(vote)
            self.votes.append(str_votes)
            f.write(str_votes+"\n")

        print "saved in cvs format under election.cvs...[done]"

    def states(self):
        all_names = []
        for line in self.votes:
            columns = line.split(',')
            all_names.append(columns[0])
        all_names.pop()
        return all_names[1:]

    def state_count(self):
        return len(self.states())

    def pretty_json(self):
        c = 0
        vote_list = []
        header = self.votes[0]
        header = ''.join([i if ord(i) < 128 else ' ' for i in header])

        header = header.split(',')
        clean_header = []

        for val in header:
            clean_header.append(val.strip().split(' ')[0])
        self.votes.pop()
        for data in self.votes[1:]:
            vote_dict = {}
            data = data.split(',')
            for value in data:
                vote_dict[clean_header[c]] = str(value)
                c += 1
            c = 0
            vote_list.append(vote_dict)
        f = open('election.json','w+')
        f.write(json.dumps(vote_list))
        print 'saved in json format under election.json...[done]'
        return json.dumps(vote_list,sort_keys=True, indent=4, separators=(',', ': '))
