if Rails.env.production?
  %w[DATABASE_URL REDIS_URL FRONTEND_ORIGIN].each do |var|
    raise KeyError, "Missing required environment variable: #{var}" unless ENV[var]
  end
end
