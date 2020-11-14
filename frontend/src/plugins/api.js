import axios from "axios"

const _api_root = "http://localhost:8000"

function get(path) {
  // returns Promise
  if (path == undefined) {
    path = "";
  }
  console.log(path);
  return axios.get(_api_root + path);
}

function healthcheck() {
  return axios.get(_api_root);
}

function registerUser(username) {
  var user = {
    "uuid": "0",
    "name": username
  }
  return axios.post(_api_root + "/user", user);
}

export default { get, healthcheck, registerUser };
