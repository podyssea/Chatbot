describe('Error handling messages for unrecognised queries is sound', function () {
    beforeEach(function () {
       cy.visit('http://localhost:3000');
       cy.get('.rsc-float-button').click();
    });

    it('Bot says that a question is outside it\'s capabilites', function () {

    });

    it('Bot asks for a rephrase', function () {

    });

    it('Bot says hello when summoned', function () {

    });

});