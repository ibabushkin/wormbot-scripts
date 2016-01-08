#!/usr/bin/env ruby
#
# Description: Returns the first result from Giphy.
# Usage: ruby giphy [search-query]
# Date: 8/1/2016

require 'open-uri'
require 'json'

if ARGV[0] == nil
  puts "Usage is: :giphy [-r] <query>"
elsif ARGV[0] == "-r"
    query = ARGV[1]
    url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=#{query}"
    source = open(url, &:read)
    parsed_source = JSON.parse(source)
    if parsed_source["data"] == []
      puts "No results found."
    else
      link = parsed_source["data"]["image_original_url"]
      puts link
    end

else
    query = ARGV[0]
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
