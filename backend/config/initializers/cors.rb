# Be sure to restart your server when you modify this file.

Rails.application.config.middleware.insert_before 0, Rack::Cors do
  allow do
    origins(
      *if Rails.env.development?
        [ENV.fetch("FRONTEND_ORIGIN", "http://localhost:3000")]
      else
        [ENV.fetch("FRONTEND_ORIGIN")]
      end
    )

    resource "/api/*",
      headers: :any,
      methods: %i[get post put patch delete options head],
      credentials: true,
      max_age: 3600
  end
end
