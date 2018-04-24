/* Menu System for Aeviternus
		Created By: Bruce Lo 2018 */

(function(){
	//Engine's create function for menu windows.
	Scene_Menu.prototype.create = function() {
    	Scene_MenuBase.prototype.create.call(this);
		    this.createCommandWindow();
		   // this.createActorPortrait();
		    this.createStatusWindow();
		    this._statusWindow.opacity = 0;

		    this.createCommandImages();
	    

	};

	Scene_Menu.prototype.createCommandImages = function(){
		this._equipButton = new Sprite();
		this._equipButton.y = 120;
		this._inventoryButton = new Sprite();
		this._inventoryButton.y = 220;
		this._configButton = new Sprite();
		this._configButton.y = 320;
		this._saveButton = new Sprite();
		this._saveButton.y = 420;
		this._gameEndButton = new Sprite();
		this._gameEndButton.y = 520;

		this.addChild(this._equipButton);
		this.addChild(this._inventoryButton);
		this.addChild(this._configButton);
		this.addChild(this._saveButton);
		this.addChild(this._gameEndButton);
		
	}

	Scene_Menu.prototype.update = function(){
		Scene_MenuBase.prototype.update.call(this);
			switch(this._commandWindow._index){
				case 0:
					this._equipButton.bitmap = ImageManager.loadPicture('equipA');//on
					this._inventoryButton.bitmap = ImageManager.loadPicture('invent');
					this._configButton.bitmap = ImageManager.loadPicture('options');
					this._saveButton.bitmap = ImageManager.loadPicture('save');
					this._gameEndButton.bitmap = ImageManager.loadPicture('end');
					break;
				case 1:
					this._equipButton.bitmap = ImageManager.loadPicture('equip');
					this._inventoryButton.bitmap = ImageManager.loadPicture('inventA');//on
					this._configButton.bitmap = ImageManager.loadPicture('options');
					this._saveButton.bitmap = ImageManager.loadPicture('save');
					this._gameEndButton.bitmap = ImageManager.loadPicture('end');
					break;
				case 2:
					this._equipButton.bitmap = ImageManager.loadPicture('equip');
					this._inventoryButton.bitmap = ImageManager.loadPicture('invent');
					this._configButton.bitmap = ImageManager.loadPicture('optionsA');//on
					this._saveButton.bitmap = ImageManager.loadPicture('save');
					this._gameEndButton.bitmap = ImageManager.loadPicture('end');
					break;
				case 3:
					this._equipButton.bitmap = ImageManager.loadPicture('equip');
					this._inventoryButton.bitmap = ImageManager.loadPicture('invent');
					this._configButton.bitmap = ImageManager.loadPicture('options');
					this._saveButton.bitmap = ImageManager.loadPicture('saveA');//on
					this._gameEndButton.bitmap = ImageManager.loadPicture('end');
					break;
				case 4:
					this._equipButton.bitmap = ImageManager.loadPicture('equip');
					this._inventoryButton.bitmap = ImageManager.loadPicture('invent');
					this._configButton.bitmap = ImageManager.loadPicture('options');
					this._saveButton.bitmap = ImageManager.loadPicture('save');
					this._gameEndButton.bitmap = ImageManager.loadPicture('endA');//on
					break;
			}//end switch

	}//end update func



	/*Scene_Menu.prototype.createActorPortrait = Function(){
			this._actorPortrait = new Sprite();
			this._actorPortrait.bitmap = ImageManager.loadPicture($gameParty.members()[0]._name);
			this.addChild(this._actorPortrait);

	};*/



	

	//Engine's function to refresh the hero's status Window ex. hpbar etc.
	Scene_Menu.prototype.start = function() {
    	Scene_MenuBase.prototype.start.call(this);
    	this._statusWindow.refresh();
	};

	//Engine's function to  handle the menu commands.
	Scene_Menu.prototype.createCommandWindow = function() {
	    this._commandWindow = new Window_MenuCommand(0, 0);
	    this._commandWindow.visible = false;
	    this._commandWindow.x = Graphics.boxWidth;
	    this._commandWindow.y = Graphics.boxHeight;
	    this._commandWindow.setHandler('equip',     this.commandPersonal.bind(this));
	    this._commandWindow.setHandler('item',      this.commandItem.bind(this));
	    this._commandWindow.setHandler('options',   this.commandOptions.bind(this));
	    this._commandWindow.setHandler('save',      this.commandSave.bind(this));
	    this._commandWindow.setHandler('gameEnd',   this.commandGameEnd.bind(this));
	    this._commandWindow.setHandler('cancel',    this.popScene.bind(this));  // need this to cancel out of the menu
	    // this._commandWindow.setHandler('skill',     this.commandPersonal.bind(this));
	    
	   // this._commandWindow.setHandler('status',    this.commandPersonal.bind(this));
	    this.addWindow(this._commandWindow);
	};

	//enables commands and sends to the specified Scene
	Window_MenuCommand.prototype.addMainCommands = function() {
    var enabled = this.areMainCommandsEnabled();
    	 if (this.needsCommand('equip')) {
	        this.addCommand(TextManager.equip, 'equip', enabled);
	    }
	    if (this.needsCommand('item')) {
	        this.addCommand(TextManager.item, 'item', enabled);
	    }
	  /*  if (this.needsCommand('skill')) {
	        this.addCommand(TextManager.skill, 'skill', enabled);
	    }
	   
	    if (this.needsCommand('status')) {
	        this.addCommand(TextManager.status, 'status', enabled);
	    }*/
	};

	Window_MenuCommand.prototype.addOptionsCommand = function() {
	    if (this.needsCommand('options')) {
	        var enabled = this.isOptionsEnabled();
	        this.addCommand(TextManager.options, 'options', enabled);
	    	}
	};

	Window_MenuCommand.prototype.addSaveCommand = function() {
	    if (this.needsCommand('save')) {
	        var enabled = this.isSaveEnabled();
	        this.addCommand(TextManager.save, 'save', enabled);
	   	}
	};

	Window_MenuCommand.prototype.addGameEndCommand = function() {
    	var enabled = this.isGameEndEnabled();
	    this.addCommand(TextManager.gameEnd, 'gameEnd', enabled);
	};

	//create BG
	Scene_Menu.prototype.createBackground = function() {
    this._backgroundSprite = new Sprite();
    this._backgroundSprite.bitmap = ImageManager.loadPicture('Night');
    this.addChild(this._backgroundSprite);
	};

	//creates menu commands
	Window_MenuCommand.prototype.makeCommandList = function() {
	    this.addMainCommands();
	    this.addOriginalCommands();
	    this.addOptionsCommand();
	    this.addSaveCommand();
	    this.addGameEndCommand();
	};

/******************************************************************************/
	// Menu Status on main menu
	Window_MenuStatus.prototype.drawItem = function(index) {
	    this.drawItemBackground(index);
	    this.drawItemImage(index);
	    this.drawItemStatus(index);
	};

	Window_MenuStatus.prototype.drawItemStatus = function(index) {
    var actor = $gameParty.members()[index];
    var rect = this.itemRect(index);
    var x = rect.x + 162;
    var y = rect.y + rect.height / 2 - this.lineHeight() * 1.5;
    var width = rect.width - x - this.textPadding();
    //this.drawActorSimpleStatus(actor, x, y, width);
    var lineHeight = this.lineHeight();
    var x2 = x + 600;//180
    var width2 = Math.min(200, width - 180 - this.textPadding());
    this.drawActorName(actor, x, y);
    this.drawActorLevel(actor, x, y + lineHeight * 1);
    this.drawActorIcons(actor, x, y + lineHeight * 2);
    //this.drawActorClass(actor, x2, y);
    this.drawActorHp(actor, x2, y + lineHeight * 1, width2);
    this.drawActorMp(actor, x2, y + lineHeight * 2, width2);


    
	};












































})();