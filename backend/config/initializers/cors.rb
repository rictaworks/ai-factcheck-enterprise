# Be sure to restart your server when you modify this file.

allowed_origins =
  if Rails.env.development?
    [
      ENV.fetch("FRONTEND_ORIGIN", "http://localhost:3000"),
      "http://localhost:3000"
    ]
  else
    [ENV.fetch("FRONTEND_ORIGIN")]
  end

Rails.application.config.middleware.insert_before 0, Rack::Cors do
  allow do
    origins(*allowed_origins)

    resource "/api/*",
      headers: :any,
      methods: %i[get post put patch delete options head],
      credentials: true,
      max_age: 3600
  end
end
