#!/usr/bin/env ruby
#
# Description: Grab gifs from Giphy.
# Usage: gif.rb [option] [argument]
# Date: 9/1/2016
#

require 'json'
require 'open-uri'

def grab_random_gif(query)
  if ARGV.length >= 3
    query = query[1..-1].join("+")
  else
    query = ARGV[0]
  end

  url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=#{query}"
  source = open(url, &:read)
  parsed_source = JSON.parse(source)

  if parsed_source["data"] == []
    puts "No results found."
  else
    puts parsed_source["data"]["image_original_url"]
  end
end

def grab_first_gif(query)
  if ARGV.length >= 2
    query = query.join("+")
  else
    query = ARGV[0]
  end

  url = "http://api.giphy.com/v1/gifs/search?q=#{query}&api_key=dc6zaTOxFJmzC"
  source = open(url, &:read)
  parsed_source = JSON.parse(source)

  if parsed_source["data"] == []
    puts "No results found."
  else
    puts parsed_source["data"][0]["images"]["fixed_height"]["url"]
  end
end
 
if ARGV[0].is_a? String

  if ARGV[0] == nil
    puts "Usage is: gif [-r random] [argument]"
  end

  if ARGV[0] == "-r"
    grab_random_gif(ARGV)
  else
    grab_first_gif(ARGV)
  end
else
  puts "Please enter a valid character."
end
