export default function handler(request, response) {
  response.status(200).json({
    message: "Halo dari HP!",
    waktu: new Date().toISOString()
  });
}
