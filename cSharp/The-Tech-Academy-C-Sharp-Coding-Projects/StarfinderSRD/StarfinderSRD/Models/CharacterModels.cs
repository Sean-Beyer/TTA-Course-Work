using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel;

namespace StarfinderSRDModelBinding.Models
{
    public class CharacterContext : DbContext
    {
        public DbSet<Character> Characters { get; set; }
        public DbSet<Race> Races { get; set; }
        public DbSet<Class> Classes { get; set; }
        public DbSet<Theme> Themes { get; set; }
    }

    public class Character
    {
        [Key, Display(Name = "ID")]
        [ScaffoldColumn(false)]
        public int CharacterID { get; set; }

        [Required, StringLength(40), Display(Name = "Name")]
        public string Name { get; set; }

        [Required, StringLength(20), Display(Name = "Race")]
        public string Race { get; set; }

        [Required, StringLength(20), Display(Name = "Class")]
        public string Class { get; set; }

        [Required, StringLength(20), Display(Name = "Theme")]
        public string Theme { get; set; }
    }

    public class Race
    {
        public int RaceID { get; set; }
        public string Name { get; set; }
        public int HP { get; set; }

        [EnumDataType(typeof(Ability)), Display(Name = "Ability Mod1")]
        public Ability Mod1 { get; set; }
        public int ModAmount1 { get; set; }

        [EnumDataType(typeof(Ability)), Display(Name = "Ability Mod2")]
        public Ability Mod2 { get; set; }
        public int ModAmount2 { get; set; }

        [EnumDataType(typeof(Ability)), Display(Name = "Ability Mod2")]
        public Ability Mod3 { get; set; }
        public int ModAmount3 { get; set; }

        [EnumDataType(typeof(Size)), Display(Name = "Size")]
        public Size Size { get; set; }

        public string Feautre1 { get; set; }
        public string Feautre2 { get; set; }
        public string Feautre3 { get; set; }
        public string Feautre4 { get; set; }
    }

    public class Class
    {
        [Key]
        public int ClassID { get; set; }
        public string Name { get; set; }
        [Display(Name = "HP/SP")]
        public int HPSP { get; set; }
        [EnumDataType(typeof(Ability)), Display(Name = "Key Ability Score")]
        public string Ability { get; set; }
        [Display(Name = "Skill Points")]
        public int SkillPoints { get; set; }
        [EnumDataType(typeof(Feature)), Display(Name = "Class Feature")]
        public string Feature { get; set; }
    }

    public class Theme
    {
        [Key]
        public int ThemeID { get; set; }
        public string Name { get; set; }
        [EnumDataType(typeof(Ability)), Display(Name = "Key Ability Score")]
        public string Ability { get; set; }
        [EnumDataType(typeof(Skills)), Display(Name = "Skill Bonus")]
        public string Skills { get; set; }
    }

    public enum Ability
    {
        Str,
        Dex,
        Con,
        Wis,
        Int,
        Cha
    }

    public enum Feature
    {
        Connections,
        Drone,
        Exocortex,
        FightingStyles,
        Improvisations,
        Specializations,
        SpellCache,
        SolarManifestation
    }

    public enum Size
    {
        Small,
        Medium,
        Large
    }

    public enum Skills
    {
        Acrobatics,
        Athletics,
        Bluff,
        Computers,
        Culture,
        Diplomacy,
        Disguise,
        Engineering,
        Intimidate,
        LifeScience,
        Medicine,
        Mysticism,
        Perception,
        PhysicalScience,
        Piloting,
        Profession,
        SenseMotive,
        SleightofHand,
        Stealth,
        Survival
    }
}