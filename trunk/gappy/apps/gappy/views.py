from django.core.template import Context, loader
from django.models.gappy import gappyusers
from django.models.auth import users
from django.utils.httpwrappers import HttpResponse, HttpResponseRedirect
from django.core.extensions import render_to_response
from django.views.decorators.auth import login_required

@login_required
def index(request):
    t = loader.get_template("gappy/index")
    c = Context({})
    return HttpResponse(t.render(c))

def login(request):
    try:
        user = users.get_object(username__exact=request.POST["username"])
        if not user.check_password(request.POST["password"]):
            raise users.UserDoesNotExist
        # set the session's user active
        request.session[users.SESSION_KEY] = user.id
        try:
            nextpage = request.GET["next"]
        except KeyError:
            nextpage = "/gappy/"
        return HttpResponseRedirect(nextpage)
    except KeyError:
        return render_to_response("gappy/login")
    except users.UserDoesNotExist:
        t = loader.get_template("gappy/login")
        c = Context({"error":"Some login information was wrong."})
        return HttpResponse(t.render(c))

def logout(request):
    try:
        del request.session[users.SESSION_KEY]
    except KeyError:
        return HttpResponse("Already logged out.")
    else:
        return HttpResponse("You have been logged out.")
