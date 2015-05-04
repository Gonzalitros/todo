json.array!(@races) do |race|
  json.extract! race, :id, :title, :country
  json.url race_url(race, format: :json)
end
