#
# Description: Pulls a random comic from the xkcd garden.
# Date: 05/04/2016
# Author: https://github.com/phildk
#

#!/usr/bin/env ruby

def grab_random_comic
  url = "https://xkcd.com/"

  random_number = Random.rand(1...1660)
  puts url + random_number.to_s
end

grab_random_comic
