require 'test_helper'

class WelcomeControllerTest < ActionController::TestCase
  test "should get aboutus" do
    get :aboutus
    assert_response :success
  end

  test "should get login" do
    get :login
    assert_response :success
  end

end
