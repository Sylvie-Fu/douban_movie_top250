	Environment:
	python 3.7.4 (in Anaconda)
	Scrapy 1.6.0

	Packages needed:
	numpy
	pandas
	matplotlib


	Notes:
	For Scrapy:
	--- DEBUG: Filtered offsite request to 'XXX'
	--- This is because a conflict occurs btw the address requested and the address patten in allow_domain parameter, so 
	try to comment out allow_domain or prohibit the filtering in Request like this: yield Request(url, callback=self.parse, dont_filter=True).

	For regex:
	--- The unicode character set for French: u00C0-u00FF
	--- The unicode character set for Chinese: u4e00-u9fa5 (extended: 0x3400-0x4db5)
	--- The unicode character set for Japanese: u0800-u4e00
	--- The unicode character set for Korean: xAC00-xD7A3
	--- The unicode character set for Russian: x0400-x052f


  
