class URL_Shortener:
    id = 1
    url2id = {}

    def shorten_url(self, original_url):
        if original_url in self.url2id:
            id = self.url2id[original_url]
            shorten_url = self.encode(id)
        else:
            self.url2id[original_url] = self.id
            shorten_url = self.encode(self.id)
            # increase cnt for next url
            self.id += 1

        return "tobedone/" + shorten_url

    def encode(self, id):
        # base 62 characters
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        ret = []
        while id > 0:
            val = id % base  ## remainder
            ret.append(characters[val])
            id = id // base ## quotient
        return "".join(ret[::-1])


shortener = URL_Shortener()
print(shortener.shorten_url("goooooooooooooogle.com"))