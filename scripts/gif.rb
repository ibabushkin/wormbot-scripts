#!/usr/bin/env ruby
#
# Description: Grab gifs from Giphy.
# Usage: gif.rb [option] [argument]
# Date: 9/1/2016
#

require 'json'
require 'open-uri'

def grab_random_gif(query)
  url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=#{query}"  
  source = open(url, &:read)
  parsed_source = JSON.parse(source)
  if parsed_source["data"] == []
    puts "No results found."
  else
    link = parsed_source["data"]["image_original_url"]
    puts link
  end
end

def grab_first_gif(query)
  url = "http://api.giphy.com/v1/gifs/search?q=#{query}&api_key=dc6zaTOxFJmzC"
  source = open(url, &:read)
  parsed_source = JSON.parse(source)
  if parsed_source["data"] == []
    puts "No results found."
  else
    link = parsed_source["data"][0]["images"]["fixed_height"]["url"]
    puts link
  end
end

def grab_first_gif_with_multiple_queries(query1, query2)
  url = "http://api.giphy.com/v1/gifs/search?q=#{query1}+#{query2}&api_key=dc6zaTOxFJmzC"
  source = open(url, &:read)
  parsed_source = JSON.parse(source)
  if parsed_source["data"] == []
    puts "No results found."
  else
    link = parsed_source["data"][0]["images"]["fixed_height"]["url"]
    puts link
  end
end

def grab_random_gif_with_multiple_queries(query1, query2)
  url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=#{query1}+#{query2}"
  source = open(url, &:read)
  parsed_source = JSON.parse(source)
  if parsed_source["data"] == []
    puts "No results found."
  else
    link = parsed_source["data"]["image_original_url"]
    puts link
  end
end

if ARGV[0] == nil
  puts "Usage is: gif [-r random] [argument]"
end

if ARGV[0] == "-r"
  query = ARGV[1]
  grab_random_gif(query)
elsif ARGV.length == 2
  grab_first_gif_with_multiple_queries(ARGV[0], ARGV[1])
elsif ARGV.length == 3
  grab_random_gif_with_multiple_queries(ARGV[1], ARGV[2])
else
  query = ARGV[0]
  grab_first_gif(query)
end

