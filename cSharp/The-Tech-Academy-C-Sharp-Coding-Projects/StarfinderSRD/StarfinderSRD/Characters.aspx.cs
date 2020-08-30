using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using StarfinderSRDModelBinding.Models;
using System.Data.Entity;
using System.Data.Entity.Infrastructure;


namespace StarfinderSRD
{
    public partial class Characters : System.Web.UI.Page
    {
        public IQueryable<Character> CharactersGrid_GetData()
        {
            CharacterContext db = new CharacterContext();
            var query = db.Characters;
            return query;
        }

        public void charactersGrid_UpdateItem(int characterID)
        {
            using (CharacterContext db = new CharacterContext())
            {
                Character item = null;
                item = db.Characters.Find(characterID);
                if (item == null)
                {
                    ModelState.AddModelError("",
                      String.Format("Item with id {0} was not found", characterID));
                    return;
                }

                TryUpdateModel(item);
                if (ModelState.IsValid)
                {
                    db.SaveChanges();
                }
            }
        }

        public void charactersGrid_DeleteItem(int characterID)
        {
            using (CharacterContext db = new CharacterContext())
            {
                var item = new Character { CharacterID = characterID };
                db.Entry(item).State = EntityState.Deleted;
                try
                {
                    db.SaveChanges();
                }
                catch (DbUpdateConcurrencyException)
                {
                    ModelState.AddModelError("",
                      String.Format("Item with id {0} no longer exists in the database.", characterID));
                }
            }
        }

        protected void Page_Load(object sender, EventArgs e)
        {

        }
    }
}