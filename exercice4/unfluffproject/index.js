//Extraction des donnes avec l outil UNFLUFF en prenant en compte les langues
//  param 1 : chemin vers le repertoire qui contiendra les fichiers de sortie
//  param 2 : chemin vers le repertoire contenant les fichiers html bruts
//  param 3 : chemin vers le fichier JSON de verite terrain pour les langues

var extractor = require('unfluff');

var fs = require('fs');
var path = require('path');

//recuperation des parametres
var args = process.argv.slice(2)

var dirOut = args[0] //repertoire de sortie
var dirHtml = args[1] //repertoire contenant les fichiers html bruts a analyser
var dirJson = args[2] //chemin vers fichier json de verite terrain pour les langues

if (dirOut && dirHtml && dirJson){

  //remplacement des / en \
  dirOut = dirOut.replace(new RegExp("/","g"),"\\")
  dirHtml = dirHtml.replace(new RegExp("/","g"),"\\")
  dirJson = dirJson.replace(new RegExp("/","g"),"\\")

  var langues = {
    "Greek": "el",
    "English": "en",
    "Russian": "ru",
    "Polish": "pl",
    "Chinese": "zh"
  };

  //lecture du fichier json
  fs.readFile(dirJson,function(err,data){
    if (err) throw err;

    let json = JSON.parse(data)

    for(var siteName in json){ //parcours de chaque site contenu dans le fichier json
        try{
          console.log(siteName+": "+json[siteName]+","+langues[json[siteName]]);
          var data = extractor(fs.readFileSync(dirHtml+"\\"+siteName),langues[json[siteName]]) //extraction du contenu
   
          //recuparation du contenu textuel et ajout des paragraphes
          var allInfos = (data.text).replace(new RegExp('\n','g'),"</p>\n<p>")
          allInfos = "<p>"+allInfos+"</p>"
          allInfos = allInfos.replace(new RegExp('\n<p></p>','g'),"")

        //sauvegarde du contenu trouve dans un nouveau fichier
        fs.writeFileSync(dirOut+"\\"+siteName,allInfos,function(err){if (err) throw err})

        }catch(error){
          console.log(error)
        }
    }
  })

}else{
  console.log("missing parameters : repertoire de sortie,repertoire contenant les fichiers html bruts a analyser,chemin vers fichier json de verite terrain pour les langues")
}

