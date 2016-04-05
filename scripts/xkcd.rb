#
# Description: ruby module for wormbot allowing integration with xkcd.
# Date: 05/04/2016
# Author: https://github.com/phildk
#

#!/usr/bin/env ruby
require 'json'
require 'nokogiri'
require 'open-uri'

def grab_number_of_latest_comic
  page = Nokogiri::HTML(open('https://xkcd.com/archive/'))
  latest_link = page.css('html body div#middleContainer > a:nth-child(5)').first['href']
  number = latest_link.delete! '/'
  return number.to_i
end

def grab_comic(number)
  url = "https://xkcd.com/#{number}/info.0.json"
  source = open(url, &:read)
  parsed_source = JSON.parse(source)

  if parsed_source["link"].empty?
    link = parsed_source['img']
  else
    link = parsed_source['link']
  end

  title = parsed_source['safe_title']
  year = parsed_source['year']

  puts "#{link} [#{year}] [#{title}]"
end

def grab_specific_comic(query, grab_number_of_latest_comic)
  max_number = grab_number_of_latest_comic
  number = ARGV[1].to_i
  if number == 0
    puts "Please enter a valid integer."
  elsif number > max_number
    puts "Please enter a number between 1 and " + max_number.to_s
  else
    grab_comic(number)
  end
end

def grab_latest_comic(grab_number_of_latest_comic)
  puts "https://xkcd.com/#{grab_number_of_latest_comic}/"
end

def grab_random_comic
  random_number = Random.rand(1..grab_number_of_latest_comic)
  grab_comic(random_number)
end

if ARGV[0] == "-n"
  grab_specific_comic(ARGV, grab_number_of_latest_comic)
elsif ARGV[0] == "-r"
  grab_random_comic
else
  grab_latest_comic(grab_number_of_latest_comic)
end
