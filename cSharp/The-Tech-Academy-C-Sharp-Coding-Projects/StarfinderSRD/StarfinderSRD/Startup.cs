using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(StarfinderSRD.Startup))]
namespace StarfinderSRD
{
    public partial class Startup {
        public void Configuration(IAppBuilder app) {
            ConfigureAuth(app);
        }
    }
}
